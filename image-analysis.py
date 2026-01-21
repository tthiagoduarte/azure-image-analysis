# Import namespaces
import os
import sys
from dotenv import load_dotenv
from PIL import Image, ImageDraw

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

def show_objects(image_file, objects):
    image = Image.open(image_file)
    draw = ImageDraw.Draw(image)

    for obj in objects:
        r = obj.bounding_box
        x1 = r.x
        y1 = r.y
        x2 = r.x + r.width
        y2 = r.y + r.height

        draw.rectangle(((x1, y1), (x2, y2)), outline="green", width=3)
        draw.text((x1, y1 - 10), obj.tags[0].name, fill="green")

    image.save("objects.jpg")

def show_people(image_file, people):
    image = Image.open(image_file)
    draw = ImageDraw.Draw(image)

    for person in people:
        if person.confidence > 0.2:
            r = person.bounding_box
            x1 = r.x
            y1 = r.y
            x2 = r.x + r.width
            y2 = r.y + r.height

            draw.rectangle(((x1, y1), (x2, y2)), outline="blue", width=3)

    image.save("people.jpg")

def main():
    load_dotenv()

    ai_endpoint = os.getenv("VISION_ENDPOINT")
    ai_key = os.getenv("VISION_KEY")

    if len(sys.argv) < 2:
        print("Usage: python image-analysis.py <image_file>")
        return

    image_file = sys.argv[1]

    try:
        cv_client = ImageAnalysisClient(
            endpoint=ai_endpoint,
            credential=AzureKeyCredential(ai_key)
        )

        with open(image_file, "rb") as f:
            image_data = f.read()

        print(f"\nAnalyzing {image_file}\n")

        result = cv_client.analyze(
            image_data=image_data,
            visual_features=[
                VisualFeatures.CAPTION,
                VisualFeatures.DENSE_CAPTIONS,
                VisualFeatures.TAGS,
                VisualFeatures.OBJECTS,
                VisualFeatures.PEOPLE],
        )

        if result.caption:
            print("\nCaption:")
            print(" Caption: '{}' (confidence: {:.2f}%)".format(
                result.caption.text, result.caption.confidence * 100))

        if result.dense_captions:
            print("\nDense Captions:")
            for caption in result.dense_captions.list:
                print(" Caption: '{}' (confidence: {:.2f}%)".format(
                    caption.text, caption.confidence * 100))

        if result.tags:
            print("\nTags:")
            for tag in result.tags.list:
                print(" Tag: '{}' (confidence: {:.2f}%)".format(
                    tag.name, tag.confidence * 100))

        if result.objects:
            print("\nObjects in image:")
            for obj in result.objects.list:
                print(" {} (confidence: {:.2f}%)".format(
                    obj.tags[0].name, obj.tags[0].confidence * 100))
            show_objects(image_file, result.objects.list)

        if result.people:
            print("\nPeople in image:")
            for person in result.people.list:
                if person.confidence > 0.2:
                    print(" {} (confidence: {:.2f}%)".format(
                        person.bounding_box, person.confidence * 100))
            show_people(image_file, result.people.list)

    except Exception as ex:
        print("ERROR:", ex)

if __name__ == "__main__":
    main()

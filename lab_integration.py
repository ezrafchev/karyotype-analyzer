
import time
import random

class LabRobot:
    def __init__(self):
        self.status = "idle"

    def prepare_sample(self, sample_id):
        print(f"Preparing sample {sample_id}")
        self.status = "preparing"
        time.sleep(2)  # Simulate preparation time
        self.status = "ready"
        return {"sample_id": sample_id, "preparation_success": random.choice([True, False])}

    def capture_image(self, sample_id):
        print(f"Capturing image for sample {sample_id}")
        self.status = "capturing"
        time.sleep(1)  # Simulate image capture time
        self.status = "idle"
        return {"sample_id": sample_id, "image_path": f"sample_{sample_id}_image.jpg"}

    def get_status(self):
        return self.status

def process_sample(robot, sample_id):
    prep_result = robot.prepare_sample(sample_id)
    if prep_result["preparation_success"]:
        image_result = robot.capture_image(sample_id)
        return image_result["image_path"]
    else:
        return None

if __name__ == "__main__":
    robot = LabRobot()
    sample_id = "12345"
    image_path = process_sample(robot, sample_id)
    if image_path:
        print(f"Image captured: {image_path}")
    else:
        print("Sample preparation failed")

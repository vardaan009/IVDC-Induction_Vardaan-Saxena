
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the road image
image = cv2.imread("road.png")

if image is None:
   raise FileNotFoundError("Could not find road.png")

# Step 2: Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 4: Display the original, grayscale, and blurred images.
plt.figure(figsize=(12,8))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

plt.subplot(1, 3, 2)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")

plt.subplot(1, 3, 3)
plt.imshow(blurred, cmap="gray")
plt.title("Gaussian Blur")

plt.tight_layout()
plt.show()


# Step 4: Apply Canny edge detection
edges = cv2.Canny(blurred, 100, 200)

# Step 5: Display the detected edges
plt.figure(figsize=(8, 6))
plt.imshow(edges, cmap="gray")
plt.title("Canny Edge Detection")
plt.show()

# Step 6: Create a Region of Interest

height, width = edges.shape

# Create a black mask with the same dimensions
mask = np.zeros_like(edges)

# Define a polygon covering the road region
polygon = np.array([
    [
        (0, height),
        (width, height),
        (width, int(height * 0.43)),
        (0, int(height * 0.43))
    ]
], dtype=np.int32)

# Fill the polygon with white
cv2.fillPoly(mask, polygon, 255)

# Keep edges only inside the polygon
roi_edges = cv2.bitwise_and(edges, mask)

# Display the ROI result
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray", vmin=0, vmax=255)
plt.title("ROI Mask")

plt.subplot(1, 2, 2)
plt.imshow(roi_edges, cmap="gray", vmin=0, vmax=255)
plt.title("Edges Inside ROI")

plt.tight_layout()
plt.show()

# Find contours in the ROI edge image
contours, hierarchy = cv2.findContours(
    roi_edges,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_SIMPLE
)

print("Number of contours detected:", len(contours))

# Draw contours on a copy of the original image
contour_image = image.copy()

cv2.drawContours(
    contour_image,
    contours,
    -1,
    (0, 255, 0),
    1
)

# Display detected contours
plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))
plt.title("Detected Contours")
plt.show()

# Step 6: Filter contours based on length

long_contours = []

for contour in contours:
    length = cv2.arcLength(contour, False)

    if length > 100:
        long_contours.append(contour)

print("Total contours:", len(contours))
print("Long contours:", len(long_contours))

# Draw only the filtered contours
filtered_image = image.copy()

cv2.drawContours(
    filtered_image,
    long_contours,
    -1,
    (0, 255, 0),
    2
)

plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
plt.title("Contours After Length Filtering")
plt.show()


# Step 7: Collect candidate boundary points

left_points = []
right_points = []

height, width = gray.shape

for contour in long_contours:
    for point in contour:
        x, y = point[0]

        # Ignore points too close to the horizon
        if y < int(height * 0.48):
            continue

        # Candidate points on the left side
        if x < int(width * 0.60):
            left_points.append((x, y))

        # Candidate points on the right side
        if x > int(width * 0.70):
            right_points.append((x, y))

print("Left candidate points:", len(left_points))
print("Right candidate points:", len(right_points))

# Visualize candidate points
candidate_image = image.copy()

for x, y in left_points:
    cv2.circle(candidate_image, (x, y), 1, (0, 255, 0), -1)

for x, y in right_points:
    cv2.circle(candidate_image, (x, y), 1, (255, 0, 0), -1)

plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(candidate_image, cv2.COLOR_BGR2RGB))
plt.title("Candidate Boundary Points")
plt.show()


# Step 8: Explore HSV colour space

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Split HSV into three channels
hue, saturation, value = cv2.split(hsv)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(hue, cmap="gray")
plt.title("Hue")

plt.subplot(1, 3, 2)
plt.imshow(saturation, cmap="gray")
plt.title("Saturation")

plt.subplot(1, 3, 3)
plt.imshow(value, cmap="gray")
plt.title("Value (Brightness)")

plt.tight_layout()
plt.show()


# Step 9: Threshold the saturation channel

threshold = 80

# Low-saturation pixels become white
_, road_mask = cv2.threshold(
    saturation,
    threshold,
    255,
    cv2.THRESH_BINARY_INV
)

# Restrict the result to our ROI
road_mask = cv2.bitwise_and(road_mask, mask)

# Display the result
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(saturation, cmap="gray")
plt.title("Saturation Channel")

plt.subplot(1, 2, 2)
plt.imshow(road_mask, cmap="gray", vmin=0, vmax=255)
plt.title("Thresholded Road Candidates")

plt.tight_layout()
plt.show()

# Step 10: Generate the final binary bitmap

final_mask = cv2.bitwise_not(road_mask)

plt.figure(figsize=(8, 6))
plt.imshow(final_mask, cmap="gray", vmin=0, vmax=255)
plt.title("Final Lane Isolation Bitmap")
plt.show()

# Save the final image
cv2.imwrite("final_lane_bitmap.png", final_mask)
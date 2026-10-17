# IVDC-Induction_Vardaan-Saxena
This is the public repository created by me to submit my induction projects given by the IVDC club for the session 2026.

## PS-01 Computer Vision.
Here my initial approach and the final approach used to get to the answer are different. The initial approach is edge based. I started with gaussian blur for canny edge detection, however that was not viable enough to create the bit-map image. The next approach for that reason was using HSV filtering to use the saturated image in order to create a final binary bit-map. I had already applied the ROI function initially which was useful for the next approach. By applying a threshold to the saturation channel and restricting the result to the Region of Interest (ROI), I generated the final binary bitmap.

## PS-02 Motion Planning.
For this problem statement, I started by creating a grid using NumPy where some cells were marked as obstacles and the remaining cells were free to move through. I then defined a starting point and a goal point and used the Breadth First Search (BFS) algorithm to find the shortest path between them. After finding the goal, I reconstructed the final path using a dictionary. Finally, I used Matplotlib to visualize the grid, showing the obstacles, explored cells, starting point, goal point and the final shortest path using different colours.

## HOW TO RUN.
Both problem statements were implemented using Python. The libraries required are **NumPy, Matplotlib and OpenCV**.
### Step 1: Install the libraries

Open your terminal and run the following command:

`pip install numpy matplotlib opencv-python`

### Step 2: PS-01 Computer Vision

1. Open the `PS-01 Computer Vision` folder.
2. Make sure `road.png` and `lane_detection.py` are in the same folder.
3. Open a terminal in that folder and run:

   `python lane_detection.py`

4. The program will display the intermediate stages of image processing, including Gaussian blur, Canny edge detection, ROI, contours and HSV filtering. The final binary bitmap will also be generated and saved as `final_lane_bitmap.png`.

### Step 3: PS-02 Motion Planning

1. Open the `PS-02 Motion Planning` folder.
2. Open a terminal in that folder and run:

   `python search_algorithm.py`

3. The program will use the **Breadth First Search (BFS)** algorithm to find the shortest path from the starting point to the goal while avoiding obstacles.
4. The final visualization will display the free cells, obstacles, explored cells, starting point, goal point and shortest path using different colours.

**Note:** PS-02 does not require any external input files, as the grid and obstacle positions are already defined in the Python code.


## USE OF AI.
I have used AI for the research purposes and writing of the code. Initially when the PS were released I spent my time on learning python. The main code initially was written using AI, which is why I have kept the comments it created. However, I had created the code step by step (which is also visible through the comments of the code) so that i could understand the workflow of the code. Since this was my first time using the libraries mentioned, I later understood the syntax and functions used here. 
### References.
Much of my research was done using AI, the workflow was simple. Paste the question and ask it to explain it to me, then i would write the summary myself in the pdf provided. In some places I have used it to give examples or bullet points in order to make the explanation more easy to understand and present. For the second problem statement I learned the search algorithms using a youtube channel *Veritasium*.

## NOTE.
I have only solved two problem statements as it was hard for me to get accommodated with the language since this was my first project in python. I wanted to put emphasis on learning what i've given nicely instead of just finishing the project. If needed, and shortlisted, i will submit the third problem statement in a given deadline after the interview. 
I will be sincerely thankful if you will consider this.

*Thankyou for reading.*

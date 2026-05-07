import cv2
import time

def main():
    cap=cv2.VideoCapture(0)

    if not cap.isOpened():  
        print("Error: Cannot open camera")
        return
    
    prev_time=0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Cannot read frame")
            break

        current_time = time.time()
        time_diff = current_time - prev_time

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
        # edges = cv2.Canny(gray_frame, 100, 200)
        edges = cv2.Canny(blurred_frame, 100, 200)

      
        fps = 1 / time_diff if time_diff > 0 else 0
        prev_time = current_time

        cv2.putText(frame, f'FPS: {fps:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        combined = cv2.hconcat([frame, edges_colored])

        
        # cv2.imshow('Original Camera Stream', frame)
        # cv2.imshow('Real-Time Camera Stream', edges)
        cv2.imshow("Original | Edge Detection", combined)
       
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    main()  
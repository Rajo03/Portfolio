import cv2

color = cv2.imread('galaxy.jpeg', 0)
cv2.imwrite('galaxy-gray.jpeg', color)
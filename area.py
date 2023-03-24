import math

def rectangle_area(length, breadth):
    return length * breadth

def circle_area(radius):
    return math.pi * radius ** 2

def triangle_area(base, height):
    return 0.5 * base * height

def display_menu():
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Right-angled Triangle")

def main():
    display_menu()
    choice = int(input("Enter your choice (1-3): "))
    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        area = rectangle_area(length, breadth)
        print(f"Rectangle with length {length} and breadth {breadth} has area {area}")
    elif choice == 2:
        radius = float(input("Enter the radius of the circle: "))
        area = circle_area(radius)
        print(f"Circle with radius {radius} has area {area}")
    elif choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = triangle_area(base, height)
        print(f"Right-angled Triangle with base {base} and height {height} has area {area}")
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
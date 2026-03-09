# 🎨 Python drawings

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)
![PyAutoGUI](https://img.shields.io/badge/Library-PyAutoGUI-green?style=for-the-badge)

A automation script that uses screen coordinates and mouse control to draw geometric shapes and spirals.

## 📋 Summary
- [Technologies](#-technologies)
- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)
- [How to Run](#-how-to-run)

---

## 🛠 Technologies
- **Python 3.x**: Core logic and mathematical calculations.
- **PyAutoGUI**: For controlling mouse movement and drag events.
- **Math Module**: Used for trigonometric functions to calculate circular paths.
- **Time Module**: Handles execution delays to allow the user to switch windows.

## ✨ Features
- **Multiple Patterns:** Choose between four distinct drawing modes: Square, Spiral Square, Circle, and Spiral Circle.
- **Screen Centering:** Automatically detects monitor resolution and starts drawing from the center of the screen.
- **Dynamic Spirals:** Uses iterative loops to increase distance or radius, creating expanding spiral effects.
- **Precise Geometry:** Implements `math.sin` and `math.cos` to translate polar coordinates into screen X/Y coordinates for perfect circles.

## 📂 Project Architecture
* `drawings.py`: The main script containing the user menu, coordinate logic, and PyAutoGUI drawing loops.

## 📚 What I Learned
* **Screen Mapping:** Retrieving and utilizing monitor dimensions for precise UI interaction.
* **Trigonometry in Code:** Applying x = r * $\cos(\theta)$ and y = r * $\sin(\theta)$ to programmatically generate circular movement.
* **Automation Timing:** Managing the `sleep` buffer to ensure the environment (like Paint) is ready before execution.

## 🔮 Future Improvements
- [ ] Add a "Cancel" hotkey to stop drawing immediately.
- [ ] Support for more complex shapes (e.g., stars or polygons).
- [ ] GUI to select shapes instead of terminal input.

## 🚀 How to Run

1. **Install dependencies:**
   This project requires `pyautogui`. Install it via pip:
   ```bash
   pip install pyautogui

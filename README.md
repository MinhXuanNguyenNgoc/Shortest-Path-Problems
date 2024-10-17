**Shortest-Path-Problems**
This is a Next.js application designed to solve various shortest path problems using different algorithms. The app leverages server-side rendering and static site generation to ensure optimal performance and scalability. The project is a Mini Project for Data Engineering, and team members can view tasks assigned to each person via the link provided below.

**Table of Contents**
Overview
Features
Tech Stack
Installation
Running the Project
Scripts
Folder Structure
Contributing
License
Overview
Shortest-Path-Problems is a web application built using Next.js, TailwindCSS, and Node.js v20.18.0. It provides a user-friendly interface for visualizing and solving shortest path problems using different algorithms such as Dijkstra’s and A*.

**Important Links:**
Repository: Shortest-Path-Problems GitHub
Tasks: Mini Project for Data Engineering - Task Assignments
Features 
Solve shortest path problems using various algorithms.
Visualize the paths and solutions in real-time.
Responsive design powered by TailwindCSS.
Server-side rendering and static site generation with Next.js.
Tech Stack
Frontend Framework: Next.js
Styling: TailwindCSS
Package Manager: NPM
Node.js: v20.18.0
Installation
To get a local copy up and running, follow these steps.

Prerequisites
Node.js v20.18.0 or higher
NPM
Clone the repository:
bash
Copy code
git clone https://github.com/MinhXuanNguyenNgoc/Shortest-Path-Problems.git
Navigate to the project directory:
bash
Copy code
cd Shortest-Path-Problems
Install dependencies:
bash
Copy code
npm install
Running the Project
To run the project in development mode:

bash
Copy code
npm run dev
Once the server starts, visit http://localhost:3000 to view the app.

Environment Variables
The API used for this project is hidden and can be found directly within the code. There is no external .env setup required, but feel free to inspect the relevant sections in the codebase to understand how the API is used.

You can use the following NPM scripts for various tasks:

npm run dev – Runs the app in development mode.
npm run build – Builds the app for production.
npm run start – Starts the production server.
npm run lint – Lints the codebase for style issues.
npm run test – Run any available tests (if applicable).
Folder Structure
The project has the following structure:

├── pages          # Next.js pages
├── public         # Static files (images, fonts, etc.)
├── components     # Reusable components
├── styles         # TailwindCSS and other styles
├── package.json   # NPM scripts and dependencies
└── README.md      # Project overview and setup instructions
Contributing
:

License
This project is licensed under the MIT License – see the LICENSE file for details.

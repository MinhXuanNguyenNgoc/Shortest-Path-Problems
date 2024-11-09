# Shortest-Path-Problems

This project visualizes the shortest path between selected points on a map using various algorithms, including Dijkstra, Bellman-Ford, Floyd-Warshall, and Yen's K-shortest paths algorithm. Built with Next.js, Leaflet, and Tailwind CSS, this application allows users to select different algorithms and see the shortest path or multiple shortest paths displayed on a map.

## Team Members
- **2470475** - Krebs Luca Felix
- **2470477** - Onuh Izuchukwu Justus
- **2470473** - Nguyen Ngoc Minh Xuan
- **2470466** - Pham Le Minh
- **2470468** - Duong Thanh Khuong

## Lecturers
- Tran Tuan Anh, Ph.D
- Nguyen An Khuong, Ph.D

## API | Backend

- Create a virtual environment using `virtualenv` module in python.

```bash
# Install module (globally)
pip install virtualenv
sudo apt install python3-virtualenv

# Generate virtual environment
virtualenv --python=<your-python-runtime-version> venv

# Activate virtual environment
source venv/bin/activate

# Install depdendency packages
pip install -r requirements.txt
```

- Run `uvicorn` web server from `backend` directory (`reload` mode is for development purposes)

```bash
uvicorn main:app --reload
```

- Go to `http://localhost:8000/docs` to see the documentation of the API
###Frontend

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started
## Project Link
[GitHub Repository](https://github.com/MinhXuanNguyenNgoc/Shortest-Path-Problems.git)

## Technologies Used
- **Next.js**: For server-side rendering and React framework
- **Leaflet**: For interactive map visualizations
- **Tailwind CSS**: For styling
- **Axios**: For making API requests to the backend
- **Leaflet**: For displaying map

---

## Getting Started

### Prerequisites
Ensure you have the following installed:
- **Node.js** (version 14 or higher)
- **npm** (usually comes with Node.js)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MinhXuanNguyenNgoc/Shortest-Path-Problems.git
   cd Shortest-Path-Problems
Install dependencies:

```bash
npm install
npm i react-leaflet
npm i axios
```

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.js`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.

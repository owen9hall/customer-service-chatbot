import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './pages/App';
import Home from './pages/Home';
import reportWebVitals from './reportWebVitals';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.css'

const router = createBrowserRouter([
  { path: "/", element: <App />},
  { path: "/home/:userID", element: <Home />},
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

reportWebVitals();

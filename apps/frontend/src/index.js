import React from "react";
import ReactDOM from "react-dom/client";

function App() {
  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>CloudShop Pro</h1>
      <p>DevOps-focused deployment demo</p>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);

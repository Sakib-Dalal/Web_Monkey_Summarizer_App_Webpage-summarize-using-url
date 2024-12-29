import React from "react";
import ReactDOM from "react-dom/client"
import axios from "axios";


function App() {
    const [url, setUrl] = React.useState("");
    const [responseData, setResponseData] = React.useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://127.0.0.1:8080/submit", { url });
            setResponseData(response.data.url);
        } catch (error) {
            console.error("Error submitting url: ", error);
        };
    };

    return (
      <div style={{textAlign: "center", marginTop: "50px"}}>
        <h1>Web Page Summarizer</h1>
        <form onSubmit={handleSubmit}>
            <input type="text" value={url} onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter Web Page URL Here"
            style={{ padding: "10px", fontSize: "16px" }}
            />
            <button type="submit"
            style={{ marginLeft: "10px",
                    padding: "10px",
                    fontSize: "16px",
                    cursor: "pointer",
                }}
            > Submit
            </button>
        </form>
        {
            responseData && (
                <h3 style={{ marginTop: "20px" }}>
                    Your Data is: {responseData}
                </h3>
            )
        }
      </div>
  );
};

export default App;
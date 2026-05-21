import { useState } from "react";

function UploadBox() {

    const [file, setFile] =
        useState(null);

    const [message, setMessage] =
        useState("");

    const [result, setResult] =
        useState("");

    const uploadFile = async () => {

        if (!file) {

            setMessage(
                "Please select CSV file"
            );

            return;
        }

        setMessage(
            "Analyzing dataset..."
        );

        setResult("");

        const formData =
            new FormData();

        formData.append(
            "file",
            file
        );

        try {

            const response =
                await fetch(
                    "http://127.0.0.1:8000/predict",
                    {
                        method: "POST",
                        body: formData
                    }
                );

            if (!response.ok) {

                throw new Error(
                    "Prediction failed"
                );
            }

            // Convert backend response
            const data =
                await response.json();

            // Store Ollama response
            setResult(
                data.prediction
            );

            setMessage(
                "Prediction completed!"
            );

        }

        catch (error) {

            console.error(error);

            setMessage(
                "Error occurred"
            );
        }
    };

    return (

        <div className="container">

            <h1>
                InferIQ
            </h1>

            <p>
                Upload your dataset
            </p>

            <input
                type="file"
                accept=".csv"
                onChange={(e) =>
                    setFile(
                        e.target.files[0]
                    )
                }
            />

            <br />

            <button
                onClick={uploadFile}
            >
                Predict Best Algorithm
            </button>

            <p>
                {message}
            </p>

            {
                result && (

                    <div
                        className="result-box"
                    >

                        <h2>
                            AI Recommendation
                        </h2>

                        <p>
                            {result}
                        </p>

                    </div>
                )
            }

        </div>
    );
}

export default UploadBox;
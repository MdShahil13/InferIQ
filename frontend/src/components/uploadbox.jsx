import { useState } from "react";

function UploadBox() {

    const [file, setFile] =
        useState(null);

    const [message, setMessage] =
        useState("");

    const uploadFile = async () => {

        if (!file) {

            setMessage(
                "Please select CSV file"
            );

            return;
        }

        setMessage(
            "Cleaning dataset..."
        );

        const formData =
            new FormData();

        formData.append(
            "file",
            file
        );

        try {

            const response =
                await fetch(
                    "http://127.0.0.1:8000/clean",
                    {
                        method: "POST",
                        body: formData
                    }
                );

            if (!response.ok) {

                throw new Error(
                    "Upload failed"
                );
            }

            const blob =
                await response.blob();

            const url =
                window.URL.createObjectURL(
                    blob
                );

            const link =
                document.createElement(
                    "a"
                );

            link.href = url;

            link.download =
                "cleaned_data.csv";

            document.body.appendChild(
                link
            );

            link.click();

            link.remove();

            window.URL.revokeObjectURL(
                url
            );

            setMessage(
                "Download completed!"
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

            <h1>InferIQ</h1>

            <p>
                Upload your noisy CSV dataset
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

            <button onClick={uploadFile}>
                Clean Dataset
            </button>

            <p>{message}</p>

        </div>
    );
}

export default UploadBox;
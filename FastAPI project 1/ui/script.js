const API_URL = "http://127.0.0.1:8000/predictions";

document.getElementById("predictBtn").addEventListener("click",predict);

async function predict(){
    const data = {
       sepal_length: Number(document.getElementById("sl").value),
        sepal_width: Number(document.getElementById("sw").value),
        petal_length: Number(document.getElementById("pl").value),
        petal_width: Number(document.getElementById("pw").value) 
    };
    try{
        const response = await fetch(`${API_URL}/`,{
            method: "POST",
            headers:{
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        document.getElementById("result").innerText=
            "Predicted Species: " + result.prediction;
 
    } catch (error) {
        document.getElementById("result").innerText =
            "Error";
    }
}
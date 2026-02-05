const API_URL = "http://127.0.0.1:8000/predictions";

async function loadData() {
    const response = await fetch(`${API_URL}/`);
    const data = await response.json();

    const table = document.getElementById("tableBody");
    table.innerHTML = "";

    data.forEach(row => {
        table.innerHTML += `
            <tr>
                <td>${row.id}</td>
                <td>${row.sepal_length}</td>
                <td>${row.sepal_width}</td>
                <td>${row.petal_length}</td>
                <td>${row.petal_width}</td>
                <td>${row.prediction}</td>
                <td>
                    <button onclick="editRecord(${row.id},
                        ${row.sepal_length},
                        ${row.sepal_width},
                        ${row.petal_length},
                        ${row.petal_width})">Edit</button>

                    <button onclick="deleteRecord(${row.id})">Delete</button>
                </td>
            </tr>
        `;
    });
}

async function deleteRecord(id) {
    await fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    });
    loadData();
}

async function editRecord(id, sl, sw, pl, pw) {

    const sepal_length = prompt("Sepal Length", sl);
    const sepal_width = prompt("Sepal Width", sw);
    const petal_length = prompt("Petal Length", pl);
    const petal_width = prompt("Petal Width", pw);

    if (
        sepal_length === null ||
        sepal_width === null ||
        petal_length === null ||
        petal_width === null
    ) return;

    await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            sepal_length: Number(sepal_length),
            sepal_width: Number(sepal_width),
            petal_length: Number(petal_length),
            petal_width: Number(petal_width)
        })
    });

    loadData();
}

loadData();

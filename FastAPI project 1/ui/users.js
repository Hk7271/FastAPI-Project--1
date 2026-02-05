const API_BASE = "http://127.0.0.1:8000";


window.onload = function () {
    loadUsers();
};


async function loadUsers() {
    const response = await fetch(`${API_BASE}/users`);
    const users = await response.json();

    const table = document.getElementById("userTable");
    table.innerHTML = "";

    users.forEach(user => {
        table.innerHTML += `
            <tr>
                <td>${user.id}</td>
                <td>${user.name}</td>
                <td>${user.email}</td>
                <td>
                    <button onclick="editUser(${user.id})">Edit</button>
                    <button onclick="deleteUser(${user.id})">Delete</button>
                </td>
            </tr>
        `;
    });
}

async function createUser() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    if (!name || !email) {
        alert("Name and Email are required");
        return;
    }

    await fetch(`${API_BASE}/users`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            email: email
        })
    });

    document.getElementById("name").value = "";
    document.getElementById("email").value = "";

    loadUsers();
}


async function editUser(id) {
    const response = await fetch(`${API_BASE}/users/${id}`);
    const user = await response.json();

    const name = prompt("Enter new name", user.name);
    if (name === null || name === "") return;

    const email = prompt("Enter new email", user.email);
    if (email === null || email === "") return;

    await fetch(`${API_BASE}/users/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            email: email,
            is_active: true
        })
    });

    loadUsers();
}

async function deleteUser(id) {
    const confirmDelete = confirm("Are you sure you want to delete this user?");
    if (!confirmDelete) return;

    await fetch(`${API_BASE}/users/${id}`, {
        method: "DELETE"
    });

    loadUsers();
}

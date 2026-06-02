const apiBase = "http://127.0.0.1:5000/api";
const notesGrid = document.getElementById("notes-grid");
const titleInput = document.getElementById("note-title");
const contentInput = document.getElementById("note-content");
const addNoteButton = document.getElementById("add-note");
const boardTitle = document.getElementById("board-title");
const greetingText = document.getElementById("greeting-text");
const currentTime = document.getElementById("current-time");
const currentDate = document.getElementById("current-date");
const adviceText = document.getElementById("advice-text");
const refreshAdviceButton = document.getElementById("refresh-advice");

async function fetchBoard() {
    try {
        const response = await fetch(`${apiBase}/board`);
        const data = await response.json();
        boardTitle.textContent = data.name || "Pizarra Dashboard";
        renderNotes(data.notes);
    } catch (error) {
        console.error("Error al cargar la pizarra:", error);
        notesGrid.innerHTML = `<div class="note-card"><h2>Error</h2><p>No se pudieron cargar las notas.</p></div>`;
    }
}

async function fetchTimeData() {
    try {
        const response = await fetch(`${apiBase}/time`);
        const data = await response.json();
        greetingText.textContent = data.greeting;
        currentTime.textContent = data.time;
        currentDate.textContent = data.date;
    } catch (error) {
        console.error("Error al cargar la hora:", error);
        greetingText.textContent = "Bienvenido a tu pizarra. No se pudo cargar la hora.";
    }
}

async function fetchAdvice() {
    try {
        adviceText.textContent = "Cargando consejo...";
        const response = await fetch(`${apiBase}/advice`);
        const data = await response.json();
        adviceText.textContent = data.advice || "Disfruta creando tu pizarra.";
    } catch (error) {
        console.error("Error al cargar el consejo:", error);
        adviceText.textContent = "No fue posible obtener el consejo. Intenta de nuevo.";
    }
}

function renderNotes(notes) {
    notesGrid.innerHTML = "";
    if (!notes.length) {
        notesGrid.innerHTML = `<div class="note-card"><h2>Sin notas</h2><p>Aún no hay notas en la pizarra.</p></div>`;
        return;
    }

    notes.forEach(note => {
        const card = document.createElement("article");
        card.className = "note-card";

        card.innerHTML = `
            <h2>${note.title}</h2>
            <p>${note.content}</p>
            <button data-id="${note.id}">Eliminar</button>
        `;

        const button = card.querySelector("button");
        button.addEventListener("click", () => deleteNote(note.id));
        notesGrid.appendChild(card);
    });
}

async function addNote() {
    const title = titleInput.value.trim();
    const content = contentInput.value.trim();
    if (!title && !content) return;

    await fetch(`${apiBase}/notes`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: title || "Nota sin título", content }),
    });

    titleInput.value = "";
    contentInput.value = "";
    await fetchBoard();
}

async function deleteNote(noteId) {
    await fetch(`${apiBase}/notes/${noteId}`, { method: "DELETE" });
    await fetchBoard();
}

addNoteButton.addEventListener("click", addNote);
refreshAdviceButton.addEventListener("click", fetchAdvice);
window.addEventListener("DOMContentLoaded", () => {
    fetchBoard();
    fetchTimeData();
    fetchAdvice();
});

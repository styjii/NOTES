const btnEditNote = document.querySelectorAll(".display-note .btn-edit")
const btnCancel = document.querySelectorAll(".update-note .btn-cancel")
const btnDeleteNote = document.querySelectorAll(".display-note .btn-delete")

btnEditNote.forEach(element => {
    element.addEventListener("click", e => {
        const displayNote = e.target.parentNode.parentNode
        const updateNote = displayNote.nextElementSibling
        updateNote.style.display = "block"
        displayNote.style.display = "none"
    })
})
btnCancel.forEach(element => {
    element.addEventListener("click", e => {
        const updateNote = e.target.parentNode.parentNode.parentNode.parentNode
        const displayNote = updateNote.previousElementSibling
        displayNote.style.display = ""
        updateNote.style.display = ""
    })
})
btnDeleteNote.forEach(element => {
    element.addEventListener("click", e => {
        const displayNote = e.target.parentNode.parentNode
        const formDeleteNote = displayNote.nextElementSibling.nextElementSibling
        
        formDeleteNote.submit()
    })
})
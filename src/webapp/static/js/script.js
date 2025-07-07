const btnEditNote = document.querySelectorAll(".display-note .btn-edit")
const btnCancelUpdateNote = document.querySelectorAll(".update-note .btn-cancel")
const btnDeleteNote = document.querySelectorAll(".display-note .btn-delete")
const btnDeleteTable = document.querySelectorAll(".btn-option .btn-delete")
const btnCancelDeleteTable = document.querySelectorAll(".btn-confirm .btn-cancel")

btnEditNote.forEach(element => {
    element.addEventListener("click", e => {
        const displayNote = e.target.parentNode.parentNode
        const updateNote = displayNote.nextElementSibling
        updateNote.style.display = "block"
        displayNote.style.display = "none"
    })
})
btnCancelUpdateNote.forEach(element => {
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
btnDeleteTable.forEach(element => {
    element.addEventListener("click", e => {
        const btnOption = e.target.parentNode
        const btnConfirm = btnOption.nextElementSibling

        btnOption.style.display = "none"
        btnConfirm.style.display = ""
    })
})
btnCancelDeleteTable.forEach(element => {
    element.addEventListener("click", e => {
        const btnConfirm = e.target.parentNode
        const btnOption = btnConfirm.previousElementSibling
        
        btnConfirm.style.display = "none"
        btnOption.style.display = ""
    })
})
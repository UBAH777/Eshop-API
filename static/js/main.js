function addReview(name, id) {
    document.getElementById("contactparent").value = id
    document.getElementById("contactcomment").innerText = '${name}, '
}
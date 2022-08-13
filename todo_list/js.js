function addTask(){
    const val = document.querySelector('input').value //Взима текста от input-a

    if (val == false) {
        alert("Cannot add empty tasks")
    }else{
    document.getElementById('task-conteiner').innerHTML+="<div class='task' onclick='this.hidden = true' >"+val+"</div>"
    }
    const clear = ""
    document.querySelector('input').value = clear
}
    function handle(e){
        if(e.keyCode === 13){
            e.preventDefault(); // Ensure it is only this code that runs

            alert("Enter was pressed was presses");
        }
    }
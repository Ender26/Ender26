function random_item(items)
{

return items[Math.floor(Math.random()*items.length)];

}



function futureTellings(){
    let tellings =["Yes", 'No','Maybe','Sure','Under No Circumstances']
    document.getElementById('txt').innerText = random_item(tellings)
}
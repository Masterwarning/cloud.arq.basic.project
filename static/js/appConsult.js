function goBack()
{
    window.location = ("/");
}

function consult_user()
{
    let id_user = document.getElementById("search").value;
    let obj_user = {"id" : id_user};

    fetch("/consult_user",{
        "method" : "post",
        "headers" : {"Content-Type" : "application/json"},
        "body" : JSON.stringify(obj_user)
    })

    .then(response => response.json())
    .then(data => {
        if(data.status === "OK")
        {   
            if(data.photo == "undefined")
            {
                document.getElementById("photo").src = "https://bucket-project-cloudvet.s3.amazonaws.com/public/defaul-photo.png"; 
            }
            else
            {
                document.getElementById("photo").src = data.photo;
            }
            
            console.log(data.object[0])
            document.getElementById("txt-id").innerHTML = "Consultar: " + data.object[0];
            document.getElementById("id").innerHTML = data.object[0];
            document.getElementById("name").innerHTML = data.object[1];
            document.getElementById("lastname").innerHTML = data.object[2];
            document.getElementById("email").innerHTML = data.object[3];
            let casting_date = (data.object[4]).replace(" 00:00:00 GMT", "") //change format
            document.getElementById("birthdate").innerHTML = casting_date;
            document.getElementById("gender").innerHTML = data.object[5];
            document.getElementById("address").innerHTML = data.object[6];
            document.getElementById("info").style.display = "block"; 
        }
        else if(data.status === "not found")
        {
            alert("Usuario no encontrado");
            document.getElementById("txt-id").innerHTML = "Consultar:";
            document.getElementById("info").style.display = "none"; 
            
        }
        else if(data.status === "error")
        {
            alert("Verificar los datos de entrada");
            document.getElementById("txt-id").innerHTML = "Consultar:";
            document.getElementById("info").style.display = "none";
        }        
    })
    .catch(error => {
        console.log(error);
        alert("Servicio no disponible, contactar al soporte");
    })



}
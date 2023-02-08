const api_key="9f4efbf38432068c7b3360d14e0b970375468301fcd82f83";
const API_URL=`https://api.dynapictures.com/designs/987deb7f3d`;
const spanError = document.getElementById('error')

async function load() {
    const res = await fetch(API_URL, {
        method: 'POST',
        headers: {
            "Authorization": "9f4efbf38432068c7b3360d14e0b970375468301fcd82f83"
        }
    });
    const data = await res.json();
    
        if (res.status !== 200) {
            spanError.innerHTML = "Hubo un error: " + res.status + data.message;
        } else {
        console.log(data)
        }

/*     const respuesta= await fetch(API_URL);
    const data =await respuesta.json();
    console.log (data);
    const img1=document.getElementById("img1");
    img1.src=data[0].url;
 */
}

load();
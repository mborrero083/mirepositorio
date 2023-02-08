const fetchData = require ("../utils/fetchData");
const Api="https://rickandmortyapi.com/api/character/";

fetchData(Api)
.then (data => {
    console.log(data.info.count);
    return fetchData(`${Api}${data.results[0].id}`);
})
.then(data =>{
    console.log(data.name)
    return fetchData (data.origin.url)
})
.then(data =>{
    console.log(data.dimension)
})
.catch(err => console.error(err));

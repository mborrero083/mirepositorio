const algopasara= () => {
    return new Promise ((resolve, reject)=> {
        if (true){
            resolve ("Hey");
        }
        else {
            reject ("whoops")
        }
    })
}

algopasara()
 .then(response => console.log (response))
 .catch (err =>console.error(err));

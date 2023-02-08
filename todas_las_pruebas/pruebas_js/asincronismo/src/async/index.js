const dosonmethingAsync= () => {
    return new Promise ((resolve,reject) =>{
        (true)
        ? setTimeout (()=> resolve ("do something async"),3000)
        : reject (new Error("test error"))
    });
}

const dosonmething = async()=> {
    const something = await dosonmethingAsync();
    console.log(something);
}

console.log ("before");
dosonmething();
console.log("after");

const anotherFunction = async () => {
    try {
      const something = await dosonmethingAsync();
      console.log(something);
    } catch (error) {
      console.error(error);
    }
  }
  
  (async () => {
    console.log('Before 1');
    await anotherFunction();
    console.log('After 1');
  })()
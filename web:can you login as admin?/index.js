(async()=>{


  function encode(str) {
    return str.replace(/[a-zA-Z]/g, function (char) {
      const isUpperCase = char === char.toUpperCase();
      const shift = isUpperCase ? 0x41 : 97;
      return String.fromCharCode((char.charCodeAt(0) - shift + 0x0D) % 26 + shift);
    });
  }
  
  
  
      await new Promise((e=>window.addEventListener("load", e))),
      document.querySelector("form").addEventListener("submit", (e=>{
          e.preventDefault();
          const r = {
              u: "input[name=username]",
              p: "input[name=password]"
          }
            , t = {};
          for (const e in r)
              t[e] = encode(btoa(document.querySelector(r[e]).value).replace(/=/g, ""));
          return "LJEgnJ4" !== t.u ? alert("Incorrect Username Try again") : "D09DH3fjBKVjIQRmLmSjnQAlZGE9" !== t.p ? alert("Incorrect Password try again") : void alert(`Congrats Your flag is ${atob(encode(t.p))}.`)
      }
      ))
  }
  )();
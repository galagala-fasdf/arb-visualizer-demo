fetch("/api/data")
  .then(res => res.json())
  .then(data => {
    document.getElementById("output").innerHTML =
      `交易对: ${data.pair} <br>
       交易所A: ${data.exchangeA} <br>
       交易所B: ${data.exchangeB}`;
  });

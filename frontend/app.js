async function sendData() {
    const input = document.getElementById('inputData').value;
    const response = await fetch(`http://localhost:5000/process/${input}`);
    const data = await response.json();
    document.getElementById('output').innerText = `Processed: ${data.processed}`;
}

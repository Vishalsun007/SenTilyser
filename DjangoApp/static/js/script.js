const audioInputArea = document.getElementById('audioInputArea');
const audioFileInput = document.getElementById('audioFileInput');
const audioPreviewContainer = document.getElementById('audioPreviewContainer');
const outputArea = document.getElementById('outputArea');
const sentimentResult = document.getElementById('sentimentResult');
const sentimentText = document.getElementById('sentimentText');

audioInputArea.addEventListener('dragover', (e) => {
  e.preventDefault();
  audioInputArea.classList.add('dragover');
});

audioInputArea.addEventListener('dragleave', (e) => {
  e.preventDefault();
  audioInputArea.classList.remove('dragover');
});

audioInputArea.addEventListener('drop', (e) => {
  e.preventDefault();
  audioInputArea.classList.remove('dragover');
  const file = e.dataTransfer.files[0];
  loadAudio(file);
});

audioFileInput.addEventListener('change', () => {
  const file = audioFileInput.files[0];
  loadAudio(file);
});

function loadAudio(file) {
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = (e) => {
    const audioPlayer = document.createElement('audio');
    audioPlayer.id = 'audioPlayer';
    audioPlayer.src = e.target.result;
    audioPlayer.controls = true;
    audioPlayer.style.maxWidth = '100%';
    audioPreviewContainer.innerHTML = '';
    audioPreviewContainer.appendChild(audioPlayer);
  };
  const formData = new FormData();
  formData.append("audio", file);


  $.ajax({
    type: "POST",
    url: "predict", 
    data: formData,
    processData: false,
    contentType: false,
    success: function (data) {
        console.log("File uploaded successfully!"); 
        sentimentText.textContent = "The audio is " + data["review"];
    },
    error: function () {
        console.error("File upload failed.");
    }
  });



  if (outputArea.style.display === 'none') {
    outputArea.style.display = 'block';
    // sentimentResult.textContent = 'Analyzing...';
    sentimentText.textContent = '';
    // Perform sentiment analysis here and update sentimentResult and sentimentText accordingly
  }
}

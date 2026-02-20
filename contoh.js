// 1. TES COPILOT: Letakkan kursor di bawah ini dan ketik: function hitungIPK
// Biarkan Copilot memberikan saran kode otomatis.

// 2. TES PRETTIER: Kode di bawah ini sengaja berantakan (spasi tidak beraturan).
// Saat kalian tekan Ctrl + S (Save), kode ini harus otomatis menjadi rapi.
const dataMahasiswa={nama:"Anak PA WR1",ipk:[3.5,3.8,3.2,3.9]};
  function cekStatus(ipk){
if(ipk>=3.5){return "Pujian"}else{return "Sangat Memuaskan"}
}

console.log(`Nama: ${dataMahasiswa.nama}`);
console.log(`Status: ${cekStatus(dataMahasiswa.ipk[3])}`);
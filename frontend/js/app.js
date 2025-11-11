new Vue({
  el: "#app",
  data: {
    name: "",
    classInfo: "",
    message: "",
    sent: false,
    sending: false,
    error: false
  },
  methods: {
    async sendMessage() {
      if (!this.message.trim()) {
        alert("Please write a message before sending 💬");
        return;
      }

      this.sending = true;
      this.sent = false;
      this.error = false;

      try {
        const response = await fetch("/save", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            name: this.name || "Anonymous",
            classInfo: this.classInfo || "Not provided",
            message: this.message
          })
        });

        const data = await response.json();

        if (data.success) {
          this.sent = true;
          this.name = "";
          this.classInfo = "";
          this.message = "";
          
          setTimeout(() => (this.sent = false), 3000);
        } else {
          this.error = true;
          console.error("Erro do servidor:", data.error);
        }
      } catch (err) {
        this.error = true;
        console.error("Erro ao enviar:", err);
      } finally {
        this.sending = false;
      }
    }
  }
});

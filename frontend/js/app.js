new Vue({
  el: "#app",
  data: {
    name: "",
    classInfo: "",
    message: "",
    feedback: "",
    sending: false,
  },
  methods: {
    async sendMessage() {
      if (!this.message.trim()) {
        this.feedback = "Please, write a message before sending.";
        return;
      }

      this.sending = true;
      this.feedback = "Sending message... 💭";

      const data = {
        name: this.name || "Anonymous",
        class: this.classInfo || "Anonymous",
        message: this.message,
      };

      try {
        const response = await fetch("http://127.0.0.1:5000/send_message", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });

        if (response.ok) {
          this.feedback = "💛 Message sent successfully! Thank you for sharing.";
          this.name = "";
          this.classInfo = "";
          this.message = "";
        } else {
          this.feedback = "⚠️ Something went wrong. Try again later.";
        }
      } catch (error) {
        console.error(error);
        this.feedback = "⚠️ Could not connect to the server. Check if Flask is running.";
      } finally {
        this.sending = false;
      }
    },
  },
});

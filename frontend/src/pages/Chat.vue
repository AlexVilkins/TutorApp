<template>
  <v-container>
    <div v-show="!dialogOpen">
      <h1>Список диалогов</h1>
      <div>
    <v-text-field
      v-model="filterText"
      label="Поиск..."
      outlined
    ></v-text-field>
  </div>
      <v-list >
        <v-list-item 
          v-for="(dialog, index) in filteredItems" 
          :key="index"
          @click="openDialog(dialog)"
        >
          <v-list-item-avatar>
            <v-icon>mdi-account-circle</v-icon>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title>{{ dialog.name }}</v-list-item-title>
            <v-list-item-subtitle>{{ dialog.lastMessage }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </div>
    <div v-show="dialogOpen">
      <v-banner  avatar="smirk.png" :stacked="false">
        <v-icon @click="closeDialog">mdi-arrow-left</v-icon>
        <v-banner-text>
          {{ selectedDialog.name }}
        </v-banner-text>
        <v-banner-avatar>
          <v-icon>mdi-account-circle</v-icon>
        </v-banner-avatar>
      </v-banner>
      <div class="chat-container" >
        <div class="chat-messages" ref="chatContainer">
          <div v-for="(message, index) in messages" :key="index" class="chat-message">
            <div class="chat-message-content" :class="{ 'chat-message-sent': message.sent, 'chat-message-received': !message.sent }">
              {{ message.text }}
            </div>
          </div>
        </div>
        <div class="chat-input">
          <v-text-field v-model="newMessage" label="Введите сообщение" outlined @keydown.enter="sendMessage"></v-text-field>
          <v-btn color="primary" @click="sendMessage">Отправить</v-btn>
        </div>
      </div>
    </div>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      dialogs: [
        { name: 'Иван Иванов', lastMessage: 'Привет, как дела?' },
        { name: 'Алексей Петров', lastMessage: 'Встретимся в 15:00?' },
        { name: 'Елена Смирнова', lastMessage: 'У нас занятие завтра' },
      ],
      messages: [
        { text: 'Привет!', sent: true },
        { text: 'Привет, как дела?', sent: false },
        { text: 'Хорошо, спасибо! А у тебя?', sent: true },
      ],
      newMessage: '',
      dialogOpen: false,
      selectedDialog: '',
      filterText: '',
      socket: null
    };
  },
  computed: {
    filteredItems() {
      return this.dialogs.filter(item => item.name.toLowerCase().includes(this.filterText.toLowerCase()));
    }
  },
  mounted() {
    const client_id = Date.now()
    this.socket = new WebSocket(`ws://localhost:8000/websockets/ws/${client_id}`);
    this.socket.onopen = () => {
      console.log('Connection successful!');
    };
  },
  methods: {
    openDialog(dialog) {
      this.selectedDialog = dialog;
      this.dialogOpen = true;
    },
    closeDialog() {
      this.dialogOpen = false;
    },
    sendMessage() {
      if (this.newMessage.trim() !== "") {

        this.socket.send(this.newMessage)
        this.newMessage = ''
        
        this.socket.onmessage = (event) => {
          this.messages.push({
            id: Date.now(),
            text: event.data.split(':')[1],
            sent: false
          })
        };

        this.$nextTick(() => {
          this.scrollToBottom();
        });
      }
    },
    scrollToBottom() {
      const chatContainer = this.$refs.chatContainer;
      chatContainer.scrollTop = chatContainer.scrollHeight;
    }
  }
};
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height:100%;
  overflow-y: auto;
}

.chat-messages {
  flex-grow: 1;
  overflow-y: auto;
  padding: 10px;
}

.chat-message {
  margin-bottom: 10px;
}

.chat-message-content {
  padding: 10px;
  border-radius: 5px;
  display: inline-block;
  max-width: 70%;
}

.chat-message-sent {
  background-color: #e0e0e0;
  align-self: flex-end;
}

.chat-message-received {
  background-color: #f5f5f5;
  align-self: flex-start;
}

.chat-input {
  display: flex;
  align-items: center;
  /* justify-items: center; */
  padding: 10px;
}

</style>
  
<template>
  <v-container>
    <h1>Список диалогов</h1>
    <v-list>
      <v-list-item 
        v-for="(dialog, index) in dialogs" 
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
    <v-dialog v-model="dialogOpen" max-width="500px">
      <v-card>
        <!-- <v-card-title>{{ selectedDialog.name }}</v-card-title>
        <v-card-text>
          <v-textarea v-model="message" label="Сообщение" required></v-textarea>
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="sendMessage">Отправить</v-btn>
          <v-btn color="secondary" @click="closeDialog">Закрыть</v-btn>
        </v-card-actions> -->
        <div class="chat-container">
      <div class="chat-messages">
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
      </v-card>
    </v-dialog>
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
      dialogOpen: false,
      // selectedDialog: null,
      // message: '',
      messages: [
        { text: 'Привет!', sent: true },
        { text: 'Привет, как дела?', sent: false },
        { text: 'Хорошо, спасибо! А у тебя?', sent: true },
      ],
      newMessage: '',
    };
  },
  methods: {
    openDialog(dialog) {
      this.selectedDialog = dialog;
      this.dialogOpen = true;
    },
    closeDialog() {
      this.selectedDialog = null;
      this.dialogOpen = false;
      this.message = '';
    },
    sendMessage() {
      if (this.newMessage.trim() !== '') {
        this.messages.push({ text: this.newMessage, sent: true });
        this.newMessage = '';
      }
    },
  }
};
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100%;
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
  padding: 10px;
}
</style>
  
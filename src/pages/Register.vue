<template>
    <div>
        <v-row class="form">
            <v-col md="4">
                <v-card class="formCard">
                    <v-text-field
                    class="field"
                        :counter="10"
                        label="Имя"
                        required
                        hide-details
                    ></v-text-field>
                    <v-text-field
                    class="field"
                        :counter="10"
                        label="Email"
                        required
                        hide-details
                    ></v-text-field>
                    <v-text-field
                    class="field"
                        :counter="10"
                        label="Пароль"
                        required
                        hide-details
                    ></v-text-field>
                    <v-btn
                        class="btn white--text justify-center"
                        color="blue"
                    >Зарегестрироваться</v-btn>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>

<style scoped>
.form {
    display: flex;
    justify-content: center;
    align-items: center;
    
}
.field {
    padding: 10px;
}

</style>
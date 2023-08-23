import { createApp } from "vue";
import { createPinia } from "pinia";

import ElementPlus from "element-plus";
import "element-plus/dist/index.css";

import 'vuetify/styles';
import { createVuetify } from "vuetify";
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

const vuetify = createVuetify({
    components,
    directives
})

import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(vuetify)
app.use(ElementPlus);

app.mount("#app");

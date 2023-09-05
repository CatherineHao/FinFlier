<template>
    <div class="container">
        <el-popover placement="right" :width="330" trigger="click">
            <template #reference>
                <div class="color">
                    <div
                        :style="{ width: '50%', height: '100%', 'background-color': `rgba(${currentColor.r}, ${currentColor.g}, ${currentColor.b}, 1)` }">
                    </div>
                    <div
                        :style="{ width: '50%', height: '100%', 'background-color': `rgba(${currentColor.r}, ${currentColor.g}, ${currentColor.b}, ${currentColor.a})` }">
                    </div>
                </div>
            </template>
            <div>
                <v-color-picker v-model="currentColor"></v-color-picker>
            </div>
        </el-popover>
    </div>
</template>
<script>
export default {
    name: "color_picker",
    props: {
        modelValue: Object
    },
    data () {
        return {
            currentColor: {
                r: 0,
                g: 0,
                b: 0,
                a: 0
            }
        };
    },
    methods: {
    },
    created () {
    },
    computed: {
    },
    mounted () {
    },
    watch: {
        modelValue: {
            handler(newValue) {
                this.currentColor = newValue;
            },
            immediate: true // 在组件创建时立即触发
        },
        // 监听currentColor的变化，并将其同步到外部modelValue
        currentColor: {
            handler(newColor) {
                // console.log(newColor.a, typeof(newColor.a));
                // if ((newColor.a) == '') newColor.a = 0
                this.$emit('update:modelValue', newColor);
                // console.log(this.currentColor);
            },
            deep: true // 监听嵌套属性的变化
        }
    },
    components: {
    }
}
</script>
<style scoped>
.container {
    display: flex;
    text-align: start;
    align-items: center;
    font-size: 14px;
}

.color {
    display: flex;
    cursor: pointer;
    height: 20px;
    width: 20px;
    background: url(data:image/svg+xml;utf8,%3Csvg%20width%3D%226%22%20height%3D%226%22%20viewBox%3D%220%200%206%206%22%20fill%3D%22none%22%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%3E%3Cpath%20d%3D%22M0%200H3V3H0V0Z%22%20fill%3D%22%23E1E1E1%22/%3E%3Cpath%20d%3D%22M3%200H6V3H3V0Z%22%20fill%3D%22white%22/%3E%3Cpath%20d%3D%22M3%203H6V6H3V3Z%22%20fill%3D%22%23E1E1E1%22/%3E%3Cpath%20d%3D%22M0%203H3V6H0V3Z%22%20fill%3D%22white%22/%3E%3C/svg%3E%0A);
}

.rgbaInput {
    width: 35px;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding-left: 3px;
    padding-right: 3px;
}

</style>

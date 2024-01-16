<template>
    <div class="square" :style="{ color: (pos ? 'green' : 'black') }">
        {{ value }}
    </div>
</template>
<script>
export default {
    props: {
        value: {
            type: Number || String,
            default: 0
        },
        pos: {
            type: Boolean,
            default: false
        }
    }
}
</script>
<style lang="scss">
.square {
    padding: 10px;
    font-weight: bold;
}
</style>
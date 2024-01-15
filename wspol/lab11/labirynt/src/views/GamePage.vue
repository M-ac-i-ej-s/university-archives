<template>
    <div>
        <div>
            game 1
        </div>
        <div>
            game 2
        </div>
    </div>
</template>
<script>
export default {
    name: 'GamePage',
    data() {
        return {
            searchArr: [
                [0,0,0,0,0,0,0,0,0,0,],
                [0,0,0,0,0,0,0,0,0,0,],
                [0,0,0,0,0,0,0,0,0,0,],
                [0,0,0,0,0,0,0,0,0,0,],
                [0,0,0,0,0,0,0,0,0,0,],
                [0,0,0,0,0,0,0,0,0,0,],
                [0,0,0,0,0,0,0,0,0,0,],
                [0,0,0,0,0,0,0,0,0,0,],
                [0,0,0,0,0,0,0,0,0,0,],
                [0,0,0,0,0,0,0,0,0,0,],
            ],       
        }
    },
    methods: {
        sockerInit() {
            /* @ts-ignore */
            socket.current = io('ws://localhost:8900')
            /* @ts-ignore */
            socket.current.emit('addUser')
            /* @ts-ignore */
            socket.current.on('startGame', data => {

            })

            socket.current.on('gameState', data => {
                console.log(data)
            })
        }
    }
}
</script>
<style lang="scss">
    
</style>
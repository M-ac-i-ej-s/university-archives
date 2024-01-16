<template>
    <div>
        <div class="game">
            <div>
                <div class="container" v-for="(row,index1) in searchArr" :key="index1">
                    <div class="container-row" v-for="(square,index2) in row" :key="index2">
                        <PoleComponent :value="square" :pos="(index1 === positionPlayerOneX && index2 === positionPlayerOneY) && true"/>
                    </div>
                </div>
            </div>
            <div v-if="gameArr">
                <div class="container" v-for="(row,index1) in gameArr" :key="index1">
                    <div class="container-row" v-for="(square,index2) in row" :key="index2">
                        <PoleComponent :value="square" :pos="(index1 === positionPlayerTwoX && index2 === positionPlayerTwoY) && true"/>
                    </div>
                </div>
            </div>
        </div>
        <div class="controls">
            <div class="controls-nav">
                <span class="controls-nav-text">
                    Player: {{ player }}
                </span>
            </div>
            <div class="controls-controls">
                <button class="controls-controls-up" @click="onMove('up')">
                    Up
                </button>
                <button class="controls-controls-left" @click="onMove('left')">
                    Left
                </button>
                <button class="controls-controls-right" @click="onMove('right')">
                    Right
                </button>
                <button class="controls-controls-down" @click="onMove('down')">
                    Down
                </button>
            </div>
        </div>
    </div>
</template>
<script>
import PoleComponent from '../components/PoleComponent.vue'
import {state, socket} from '../socket/index.js'

export default {
    name: 'GamePage',
    components: {
        PoleComponent
    },
    data() {
        return {
            searchArr: [
                [9,9,9,9,9,9,9,9,9,9,9,9],
                [9,0,0,0,0,0,0,0,0,0,0,9],
                [9,0,0,0,0,0,0,0,0,0,0,9],
                [9,0,0,0,0,0,0,0,0,0,0,9],
                [9,0,0,0,0,0,0,0,0,0,0,9],
                [9,0,0,0,0,0,0,0,0,0,0,9],
                [9,0,0,0,0,0,0,0,0,0,0,9],
                [9,0,0,0,0,0,0,0,0,0,0,9],
                [9,0,0,0,0,0,0,0,0,0,0,9],
                [9,0,0,0,0,0,0,0,0,0,0,9],
                [9,0,0,0,0,0,0,0,0,0,0,9],
                [9,9,9,9,9,9,9,9,9,9,9,9]
            ],    
        }
    },
    methods: {
        onMove(move) {
            if(state.player === 'One') {
                socket.emit('PlayerOneMove', move)

                socket.on('PlayerOneMove', data => {
                    if(data.mess === 'win') {
                        alert('Player One win')
                    } else if(data.mess === 'ok') {
                        state.positionPlayerOne = data.startPoint1
                        location.reload()
                    } else {
                        alert('oops, there is a wall')
                    }
                })
            } else {
                socket.emit('PlayerTwoMove', move)

                socket.on('PlayerTwoMove', data => {
                    if(data.mess === 'win') {
                        alert('Player Two win')
                    } else if(data.mess === 'ok') {
                        location.reload()

                        state.positionPlayerTwo = data.startPoint1
                    } else {
                        alert('oops, there is a wall')
                    }
                })
            }
        }
    },
    computed: {
        gameArr() {
            this.gameArr = state.gameArr
            this.searchArr[state.positionPlayerOne.x][state.positionPlayerOne.y] = 'O'
            return state.gameArr
        },
        positionPlayerOneX() {
            return state.positionPlayerOne.x
        },
        positionPlayerOneY() {
            return state.positionPlayerOne.y
        },
        positionPlayerTwoX() {
            return state.positionPlayerTwo.x
        },
        positionPlayerTwoY() {
            return state.positionPlayerTwo.y
        },
        player() {
            return state.player
        },
    },
}

</script>
<style lang="scss">
.game {
    display: flex;
    justify-content: center;
    gap: 30px
}
.container {
    display: flex;
}
</style>
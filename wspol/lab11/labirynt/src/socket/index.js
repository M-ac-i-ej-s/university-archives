import { defineStore } from "pinia";
import {io} from 'socket.io-client'

export const socket = io('ws://localhost:8900')

export const useItemStore = defineStore("item", {
    state: () => ({
        gameArr: null,
        positionPlayerOne: null,
        positionPlayerTwo: null,
        player: null,
    }),
  
    actions: {
      bindEvents() {
        socket.emit('addUser')

        socket.on('startGame', data => {
            console.log(data)
            if(!this.gameArr) {
                this.gameArr = data.PlayerTwoLabirynth
                this.player = 'Two'
                this.positionPlayerTwo = data.startPoint2
                this.positionPlayerOne = data.startPoint1
            }
        })

        socket.on('waiting', data => {
            this.gameArr = data.PlayerOneLabirynth
            this.player = 'One'
            this.positionPlayerTwo = data.startPoint1
            this.positionPlayerOne = data.startPoint2
        })
      },
  
      startGame() {
      },
    },
  });
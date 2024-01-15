<template>
    <div class="Welcome">
        <div class="welcome-nav">
            <span class="welcome-nav-text">
                Welcome to
            </span>
            <span class="welcome-nav-title">
                The Maze!
            </span>
        </div>
        <div class="welcome-controls">
            <router-link to="/game">
                <button class="welcome-controls-start">
                    Start
                </button>
            </router-link>
        </div>
    </div>
</template>
<script>
export default {
    
}
</script>
<style lang="scss">
.Welcome {
    padding: 250px 0 0 0;
    .welcome-nav {
        display: flex;
        flex-direction: column;
        align-items: center;
        .welcome-nav-text {
            font-size: 25px;
        }
        .welcome-nav-title {
            font-size: 50px;
        }
    }
    .welcome-controls {
        padding: 50px 0 0 0;
        .welcome-controls-start {
            font-size: 40px;
            padding: 10px 20px;
            border-radius: 20px;
            border: 0;
            background-color: rgb(107, 216, 180);
            cursor: pointer;
            transition: 0.5s ease-in-out;
            color: black;
            &:hover {
                background-color: rgb(26, 52, 100);
                color: white;
            }
        }
    }
}
</style>
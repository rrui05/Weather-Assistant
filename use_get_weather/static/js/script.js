document.addEventListener('DOMContentLoaded', () => {
    const chatHistory = document.getElementById('chat-history');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const timeEl = document.getElementById('current-time');

    // 显示时间
    function updateTime() {
        const now = new Date();
        timeEl.innerText = now.toLocaleString();
    }
    updateTime();

    // 发送消息函数
    const sendMessage = async () => {
        const input = userInput.value.trim();
        if (!input) return;

        // 添加用户消息到历史记录
        addMessageToHistory(input, 'user');
        userInput.value = '';

        try {
            // 显示加载状态
            addLoadingIndicator();

            // 发送请求到后端
            const response = await fetch('/query', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ input: input })
            });

            // 移除加载状态
            removeLoadingIndicator();

            if (response.ok) {
                const data = await response.json();
                addMessageToHistory(data.response, 'bot');
            } else {
                const error = await response.json();
                addMessageToHistory(`⚠️ ${error.error}`, 'bot');
            }
        } catch (error) {
            removeLoadingIndicator();
            addMessageToHistory('网络错误，请稍后再试', 'bot');
            console.error('Error:', error);
        }
    };

    const addMessageToHistory = (text, sender) => {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;

        const avatarDiv = document.createElement('div');
        avatarDiv.className = `avatar ${sender}-avatar`;
        avatarDiv.innerHTML = sender === 'user' ?
            '<i class="fas fa-user"></i>' :
            '<i class="fas fa-robot"></i>';

        const contentDiv = document.createElement('div');
        contentDiv.className = 'content';
        contentDiv.innerHTML = text.replace(/\n/g, '<br>');

        // 统一使用appendChild的顺序，通过CSS的flex-direction控制显示位置
        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(contentDiv);

        chatHistory.appendChild(messageDiv);
        scrollToBottom();
    };
    // 添加加载指示器
    const addLoadingIndicator = () => {
        const loadingDiv = document.createElement('div');
        loadingDiv.className = 'message bot-message';
        loadingDiv.id = 'loading-indicator';

        const avatarDiv = document.createElement('div');
        avatarDiv.className = 'avatar bot-avatar';
        avatarDiv.innerHTML = '<i class="fas fa-robot"></i>';

        const contentDiv = document.createElement('div');
        contentDiv.className = 'content';
        contentDiv.innerHTML = '<div class="loading"><span></span><span></span><span></span></div>';

        loadingDiv.appendChild(avatarDiv);
        loadingDiv.appendChild(contentDiv);
        chatHistory.appendChild(loadingDiv);
        scrollToBottom();
    };

    const removeLoadingIndicator = () => {
        const loadingDiv = document.getElementById('loading-indicator');
        if (loadingDiv) loadingDiv.remove();
    };

    // 滚动到底部
    const scrollToBottom = () => {
        chatHistory.scrollTop = chatHistory.scrollHeight;
    };

    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });
});
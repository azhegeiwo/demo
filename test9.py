import tkinter as tk
import random
from tkinter import messagebox

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('高一七班人员名单')
        self.checkbutton_vars = []
        self.interface()

    def interface(self):
        """界面布局"""
        # 输入框部分
        input_frame = tk.Frame(self.root)
        input_frame.grid(row=0, column=0, columnspan=5, sticky="ew", padx=5, pady=5)
        
        tk.Label(input_frame, text="抽取人数：").pack(side="left")
        self.draw_num_entry = tk.Entry(input_frame, width=8)
        self.draw_num_entry.pack(side="left", padx=5)
        
        tk.Button(
            input_frame, 
            text="开始抽取",
            command=self.confirm_draw
        ).pack(side="left", padx=5)

        # 复选框区域
        list_frame = tk.LabelFrame(self.root, text="参与抽取人员（请勾选）")
        list_frame.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

        # 配置网格列均匀分布
        for col in range(5):
            list_frame.columnconfigure(col, weight=1, uniform="cols")

        # 计算最大名字长度用于统一宽度
        max_name_len = max(len(name) for name in self.all_names)
        check_width = max_name_len + 1  # 增加1个字符余量

        # 生成复选框
        for idx, name in enumerate(self.all_names):
            var = tk.BooleanVar(value=True)
            self.checkbutton_vars.append(var)
            
            cb = tk.Checkbutton(
                list_frame,
                text=name,
                variable=var,
                anchor="w",
                width=check_width,  # 统一宽度
                padx=5,
                pady=2
            )
            row, col = divmod(idx, 5)
            cb.grid(row=row, column=col, sticky="w")

        # 配置根窗口自适应
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)

    def confirm_draw(self):
        """处理抽取逻辑"""
        try:
            num = int(self.draw_num_entry.get())
            if num <= 0:
                raise ValueError
            
            candidates = [
                name 
                for name, var in zip(self.all_names, self.checkbutton_vars) 
                if var.get()
            ]
            
            if not candidates:
                messagebox.showwarning("警告", "请至少勾选一个参与者！")
                return
                
            if num > len(candidates):
                messagebox.showwarning(
                    "人数不足",
                    f"当前勾选{len(candidates)}人，少于需要抽取的{num}人！"
                )
                return
                
            result = random.sample(candidates, num)
            messagebox.showinfo(
                "抽取结果",
                f"成功抽取{num}人：\n" + "\n".join(result)
            )
            
        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的正整数！")

    all_names = [
        #输入姓名加冒号，每个姓名用逗号隔开
    ]

if __name__ == '__main__':
    app = GUI()
    app.root.mainloop()
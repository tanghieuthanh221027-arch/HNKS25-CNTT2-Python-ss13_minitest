staff_list = [
    {
        'id' : 101,
        'staff_name' : 'Nguyen Van A',
        'salary' : 10.0
    },
    {
        'id' : 102,
        'staff_name' : 'Le Thi B',
        'salary' : 15.5
    }
]

while True : 
    choice = input('''
QUẢN LÝ NHÂN SỰ - STAFF MANAGER
1. Thêm nhân viên mới
2. Danh sách nhân viên
3. Tìm kiếm nhân viên theo mã
4. Xóa nhân viên khỏi hệ thống
5. Thoát chương trình
                   
Nhập lựa chọn của bạn (1-5) : ''')
    
    if not choice.isdigit():
        print('Lựa chọn không hợp lệ ! Nhập từ 1-5 !')
    
    choice = int(choice)

    if choice == 1:
        new_staff_name = input('Nhập tên nhân viên mới : ').strip().title()
        if new_staff_name == ' ':
            print('Tên nhân viên không được để trống !')
            continue
        
        while True : 
            new_salary = float(input('Nhập lương mới : '))
            if new_salary < 0 or new_salary == ' ':
                print('Mức lương không hợp lệ !')
                continue
            else : 
                break

        new_staff = {
            'id' : len(staff_list) + 1,
            'staff_name' : new_staff_name,
            'salary' : new_salary
        }

        staff_list.append(new_staff)
        print(f'Thêm nhân viên mới thành công ! ID : {new_staff['id']}')

    elif choice == 2: 
        print('Danh sách nhân viên hiện tại')
        if len(staff_list) == 0 :
            print('Chưa có dữ liệu nhân sự!')
            continue

        else :
            print('ID | Tên nhân viên | Mức lương')
            for index , staff in enumerate(staff_list , start=101):
                print(f'{index :<5} | {staff['staff_name'] :<10} | {staff['salary'] :<5}')
            
    elif choice == 3:
        find_staff_id = input('Nhập id nhân viên cần tìm : ')

        if not find_staff_id.isdigit():
            print('Mã id nhập vào phải là số !')
            continue
        for staff_find in staff_list:
            if staff_find['id'] == find_staff_id:
                print(staff_find)

    elif choice == 5:
        print('Thoát chương trình !')
        break
    else :
        print('Lựa chọn không hợp lệ !')
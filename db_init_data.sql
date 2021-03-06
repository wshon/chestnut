
INSERT INTO T_ADMIN_ROLE (F_ADMIN_ROLE_ID, F_ADMIN_ROLE_NAME, F_ADMIN_ROLE_DESC) VALUES (1, '超级管理员', '超级管理员');

INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (1, 0, 1, 'system', '', '', '&#xe6b8;', '用户与权限', '管理员权限');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (2, 1, 1, 'system', 'admin', '', '', '管理员管理', '管理员管理');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (3, 2, 1, 'system', 'admin', 'index', '', '管理员管理', '管理员管理');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (4, 2, 1, 'system', 'admin', 'new', '', '添加管理员', '添加管理员');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (5, 2, 0, 'system', 'admin', 'select', '', '获取管理员接口', '获取管理员接口');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (6, 2, 0, 'system', 'admin', 'create', '', '添加管理员接口', '添加管理员接口');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (7, 2, 0, 'system', 'admin', 'update', '', '更新管理员接口', '更新管理员接口');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (8, 2, 0, 'system', 'admin', 'delete', '', '删除管理员接口', '删除管理员接口');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (9, 1, 1, 'system', 'role', '', '', '角色管理', '角色管理');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (10, 9, 1, 'system', 'role', 'index', '', '角色管理', '角色管理');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (11, 9, 1, 'system', 'role', 'new', '', '角色管理', '角色管理');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (12, 9, 0, 'system', 'role', 'select', '', '角色管理', '角色管理');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (13, 9, 0, 'system', 'role', 'create', '', '角色管理', '角色管理');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (14, 9, 0, 'system', 'role', 'update', '', '角色管理', '角色管理');
INSERT INTO T_ADMIN_RIGHT (F_ADMIN_RIGHT_ID, F_ADMIN_RIGHT_PARENT_ID, F_ADMIN_RIGHT_IS_MENU, F_ADMIN_RIGHT_GROUP, F_ADMIN_RIGHT_MODEL, F_ADMIN_RIGHT_ACTION, F_ADMIN_RIGHT_ICON, F_ADMIN_RIGHT_NAME, F_ADMIN_RIGHT_DESC) VALUES (15, 9, 0, 'system', 'role', 'delete', '', '角色管理', '角色管理');

INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (1, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (2, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (3, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (4, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (5, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (6, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (7, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (8, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (9, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (10, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (11, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (12, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (13, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (14, 1);
INSERT INTO T_ADMIN_ROLE_RIGHT_RL (F_ADMIN_RIGHT_ID, F_ADMIN_ROLE_ID) VALUES (15, 1);

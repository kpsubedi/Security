from ctypes import *
# Let's map the Microsoft types to ctypes for clarity
BYTE = c_ubyte
WORD = c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p
PVOID = c_void_p
LPVOID = c_void_p
UINT_PTR = c_ulong
SIZE_T = c_ulong
UINT_PTR = c_ulong
# Constants 
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010
DBG_CONTINUE = 0x00010002
PROCESS_ALL_ACCESS = 0x001F0FFF
INFINITE = 0xFFFFFFFF

THREAD_ALL_ACCESS = 0x001F03FF
TH32CS_SNAPTHREAD = 0x00000004

CONTEXT_FULL = 0x00010007
CONTEXT_DEBUG_REGISTERS = 0x00010010

#Debug Event Constatn
EXCEPTION_DEBUG_EVENT = 0x1

EXCEPTION_ACCESS_VIOLATION = 0xC0000005
EXCEPTION_BREAKPOINT = 0x80000003
EXCEPTION_GUARG_PAGE = 0x80000001
EXCEPTION_SINGLE_STEP = 0x80000004
# Structures for CreateProcess() function
# http://msdn.microsoft.com/en-us/library/windows/desktop/ms686331%28v=vs.85%29.aspx
#typedef struct _STARTUPINFO {
#  DWORD  cb;
#  LPTSTR lpReserved;
#  LPTSTR lpDesktop;
#  LPTSTR lpTitle;
#  DWORD  dwX;
#  DWORD  dwY;
#  DWORD  dwXSize;
#  DWORD  dwYSize;
#  DWORD  dwXCountChars;
#  DWORD  dwYCountChars;
#  DWORD  dwFillAttribute;
#  DWORD  dwFlags;
#  WORD   wShowWindow;
#  WORD   cbReserved2;
#  LPBYTE lpReserved2;
#  HANDLE hStdInput;
#  HANDLE hStdOutput;
#  HANDLE hStdError;
# } STARTUPINFO, *LPSTARTUPINFO;
class STARTUPINFO(Structure):
	_fields_ = [
		("cb",			DWORD),
		("lpReserved",			LPTSTR),
		("lpDesktop",			LPTSTR),
		("lpTitle",				LPTSTR),
		("dwX",				DWORD),
		("dwY",			DWORD),
		("dwXSize",			DWORD),
		("dwYSize",			DWORD),
		("dwXCountChars",			DWORD),
		("dwYCountChars",			DWORD),
		("dwFillAttribute",			DWORD),
		("dwFlags",			DWORD),
		("wShowWindow",			WORD),
		("cbReserved2",			WORD),
		("lpReserved2",			LPBYTE),
		("hStdInput",			HANDLE),
		("hStdOutput",			HANDLE),
		("hStdError",			HANDLE),
	]
# http://msdn.microsoft.com/en-us/library/windows/desktop/ms684873%28v=vs.85%29.aspx
#typedef struct _PROCESS_INFORMATION {
#  HANDLE hProcess;
#  HANDLE hThread;
#  DWORD  dwProcessId;
#  DWORD  dwThreadId;
#} PROCESS_INFORMATION, *LPPROCESS_INFORMATION;
class PROCESS_INFORMATION(Structure):
	_fields_ = [
		("hProcess",			HANDLE),
		("hThread",				HANDLE),
		("dwProcessId",			DWORD),
		("dwThreadId",			DWORD),
	]
#
# http://msdn.microsoft.com/en-us/library/windows/desktop/ms679308%28v=vs.85%29.aspx
#typedef struct _DEBUG_EVENT {
#  DWORD dwDebugEventCode;
#  DWORD dwProcessId;
#  DWORD dwThreadId;
#  union {
#    EXCEPTION_DEBUG_INFO      Exception;
#    CREATE_THREAD_DEBUG_INFO  CreateThread;
#    CREATE_PROCESS_DEBUG_INFO CreateProcessInfo;
#    EXIT_THREAD_DEBUG_INFO    ExitThread;
#    EXIT_PROCESS_DEBUG_INFO   ExitProcess;
#    LOAD_DLL_DEBUG_INFO       LoadDll;
#    UNLOAD_DLL_DEBUG_INFO     UnloadDll;
#    OUTPUT_DEBUG_STRING_INFO  DebugString;
#    RIP_INFO                  RipInfo;
#  } u;
#} DEBUG_EVENT, *LPDEBUG_EVENT;

#For more information http://msdn.microsoft.com/en-us/library/windows/desktop/aa363082(v=vs.85).aspx
#typedef struct _EXCEPTION_RECORD {
#  DWORD                    ExceptionCode;
#  DWORD                    ExceptionFlags;
#  struct _EXCEPTION_RECORD  *ExceptionRecord;
#  PVOID                    ExceptionAddress;
#  DWORD                    NumberParameters;
#  ULONG_PTR                ExceptionInformation[EXCEPTION_MAXIMUM_PARAMETERS];
#} EXCEPTION_RECORD, *PEXCEPTION_RECORD;
class EXCEPTION_RECORD(Structure):
	pass
EXCEPTION_RECORD._fields_ = [
		("ExceptionCode",			DWORD),
		("ExceptionFlags",			DWORD),
		("ExceptionRecord",			POINTER(EXCEPTION_RECORD)),
		("ExceptionAddress",		PVOID),
		("NumberParameters",		DWORD),
		("ExceptionInformation",	UINT_PTR * 15),

	]
#class EXCEPTION_RECORD(Structure):
#	_fields_ = [
#		("ExceptionCode",			DWORD),
#		("ExceptionFlags",			DWORD),
#		("ExceptionRecord",			POINTER(EXCEPTION_RECORD)),
#		("ExceptionAddress",		PVOID),
#		("NumberParameters",		DWORD),
#		("ExceptionInformation",	UINT_PTR * 15),
#	]
# For more info http://msdn.microsoft.com/en-us/library/windows/desktop/ms679326%28v=vs.85%29.aspx
#typedef struct _EXCEPTION_DEBUG_INFO {
#  EXCEPTION_RECORD ExceptionRecord;
#  DWORD            dwFirstChance;
#} EXCEPTION_DEBUG_INFO, *LPEXCEPTION_DEBUG_INFO;
#
class EXCEPTION_DEBUG_INFO(Structure):
	_fields_ = [
		("ExceptionRecord",			EXCEPTION_RECORD),
		("dwFirstChance",			DWORD),
	]
# It populates UNION 
class DEBUG_EVENT_UNION(Union):
	_fields_ = [
		("Exception",			EXCEPTION_DEBUG_INFO),
#		("CreateThread",		CREATE_THREAD_DEBUG_INFO),
#		("CreateProcessInfo",	CREATE_PROCESS_DEBUG_INFO),
#		("ExitThread",			EXIT_THREAD_DEBUG_INFO),
#		("ExitProcess",			EXIT_PROCESS_DEBUG_INFO),
#		("LoadDll",				LOAD_DLL_DEBUG_INFO),
#		("UnloadDll",			UNLOAD_DLL_DEBUG_INFO),
#		("DebugString",			OUTPUT_DEBUG_STRING_INFO),
#		("RipInfo",				RIP_INFO),
	]

# It populates DEBUG_EVENT Structure

class DEBUG_EVENT(Structure):
	_fields_ = [
		("dwDebugEventCode",			DWORD),
		("dwProcessId",					DWORD),
		("dwThreadId",					DWORD),
		("u",							DEBUG_EVENT_UNION), # Union from above
	]
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms686735%28v=vs.85%29.aspx
#typedef struct tagTHREADENTRY32 {
#  DWORD dwSize;
#  DWORD cntUsage;
#  DWORD th32ThreadID;
#  DWORD th32OwnerProcessID;
#  LONG  tpBasePri;
#  LONG  tpDeltaPri;
#  DWORD dwFlags;
#} THREADENTRY32, *PTHREADENTRY32;
class THREADENTRY32(Structure):
	_fields_ = [
			("dwSize",			DWORD),
			("cntUsage",		DWORD),
			("th32ThreadID",	DWORD),
			("th32OwnerProcessID",DWORD),
			("tpBasePri",		DWORD),
			("tpDeltaPri",		DWORD),
			("dwFlags",			DWORD),
	]

# https://msdn.microsoft.com/en-us/library/windows/desktop/ms679284(v=vs.85).aspx
#typedef struct _CONTEXT {
#DWORD ContextFlags;
#DWORD Dr0;
#DWORD Dr1;
#DWORD Dr2;
#DWORD Dr3;
#DWORD Dr6;
#DWORD Dr7;
#FLOATING_SAVE_AREA FloatSave;
#DWORD SegGs;
#DWORD SegFs;
#DWORD SegEs;
#DWORD SegDs;
#DWORD Edi;
#DWORD Esi;
#DWORD Ebx;
#DWORD Edx;
#DWORD Ecx;
#DWORD Eax;
#DWORD Ebp;
#DWORD Eip;
#DWORD SegCs; // MUST BE SANITIZED
#DWORD EFlags; // MUST BE SANITIZED
#DWORD Esp;
#DWORD SegSs;
#BYTE ExtendedRegisters[MAXIMUM_SUPPORTED_EXTENSION];
#} CONTEXT;	

# http://www.nirsoft.net/kernel_struct/vista/FLOATING_SAVE_AREA.html
#typedef struct _FLOATING_SAVE_AREA
#{
#     ULONG ControlWord;
#     ULONG StatusWord;
#     ULONG TagWord;
#     ULONG ErrorOffset;
#     ULONG ErrorSelector;
#     ULONG DataOffset;
#     ULONG DataSelector;
#     UCHAR RegisterArea[80];
#     ULONG Cr0NpxState;
#} FLOATING_SAVE_AREA, *PFLOATING_SAVE_AREA;

class FLOATING_SAVE_AREA(Structure):
	_fields_ = [
		("ControlWord",			DWORD),
		("StatusWord",			DWORD),
		("TagWord",				DWORD),
		("ErrorOffset",			DWORD),
		("ErrorSelector",		DWORD),
		("DataOffset",			DWORD),
		("DataSelector",		DWORD),
		("RegisterArea",		BYTE * 80),
		("Cr0NpxState",			DWORD),
	]
# CONTEXT Structure used above FLOATING_SAVE_AREA structure
class CONTEXT(Structure):
	_fields_ = [
		("ContextFlags",	DWORD),
		("Dr0",				DWORD),
		("Dr1",				DWORD),
		("Dr2",				DWORD),
		("Dr3",				DWORD),
		("Dr6",				DWORD),
		("Dr7",				DWORD),
		("FloatSave",		FLOATING_SAVE_AREA),
		("SegGs",			DWORD),
		("SegFs",			DWORD),
		("SegEs",			DWORD),
		("SegDs",			DWORD),
		("Edi",				DWORD),
		("Esi",				DWORD),
		("Ebx",				DWORD),
		("Edx",				DWORD),
		("Ecx",				DWORD),
		("Eax",				DWORD),
		("Ebp",				DWORD),
		("Eip",				DWORD),
		("SegCs",			DWORD),
		("EFlags",			DWORD),
		("Esp",				DWORD),
		("SegSs",			DWORD),
		("ExtendedRegisters",	BYTE * 512),
	]


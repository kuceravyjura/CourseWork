#include <iostream>
#include <iomanip>
#include <fstream>
#include <filesystem>
#include <string>
#include <ctime>

#include "include/cpp_httplib/httplib.h"

using namespace httplib;
using namespace std;

void gen_response(const Request& req, Response& res) {
    const auto& ret = req.get_file_value("data.bak");
    auto reg = req.has_file("data.bat");
    auto ren = req.has_file("data.dir");
    cout << '\t ' << reg << '\t ' << ren << '\t';
    string save1 = "data.bak";
    string save2 = "data.bat";
    string save3 = "data.dir";
    

}


int main() {
    Server svr;
    svr.Post("/", gen_response);
    cout << "Start server... OK\n";
    svr.listen("localhost", 3000);
}
